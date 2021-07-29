"""DNS Authenticator for UltraDNS."""
import ultra_rest_client
import zope.interface

from certbot import interfaces
from certbot.plugins import dns_common
from certbot.plugins.dns_common import CredentialsConfiguration

# udns values
username = 'USERNAME'
password = 'PASSWORD'
use_http = 'False'
udns_endpoint = 'restapi.ultradns.com'

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for UltraDNS"""
    description = 'make changes to TXT records in domains hosted with UDNS'
    ttl = 60

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.credentials: Optional[CredentialsConfiguration] = None
        self.c = ultra_rest_client.RestApiClient(username, password, 'True' == use_http, udns_endpoint)

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super().add_parser_arguments(add, default_propagation_seconds=60)
        pass

    def more_info(self):
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 challenge using "
            + "the UltraDNS REST API."
        )

    def _setup_credentials(self):
        self.credentials = None

    def _perform(self, domain, validation_name, validation):
        self._udnsclient().create(domain, "TXT", validation_name, 300, validation)

    def _cleanup(self, domain, validation_name, validation):
        self._udnsclient().delete(domain, "TXT", validation_name)

    def _udnsclient(self):
        return UDNSClient(username, password)

class UDNSClient:
    """do the work"""
    def __init__(self, username, password):
        self.c = ultra_rest_client.RestApiClient(username, password, 'True' == use_http, udns_endpoint)

    def create(self, domain, record_type, record, ttl, value):
        self.c.create_rrset(domain, record_type, record, ttl, value)

    def delete(self, domain, record_type, record):
        self.c.delete_rrset(domain, record_type, record)
