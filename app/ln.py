import sys
import os
sys.path.append('/app/proto')

import rpc_pb2 as lnrpc
import rpc_pb2_grpc as rpcstub
import grpc


# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'




import codecs

# Lnd admin macaroon is at ~/.lnd/data/chain/bitcoin/simnet/admin.macaroon on Linux and
# ~/Library/Application Support/Lnd/data/chain/bitcoin/simnet/admin.macaroon on Mac
with open('/data/.lnd/data/chain/bitcoin/testnet/admin.macaroon', 'rb') as f:
    macaroon_bytes = f.read()
    macaroon = codecs.encode(macaroon_bytes, 'hex')

def metadata_callback(context, callback):
    # for more info see grpc docs
    callback([('macaroon', macaroon)], None)

# Lnd cert is at ~/.lnd/tls.cert on Linux and
# ~/Library/Application Support/Lnd/tls.cert on Mac
cert = open('/data/.lnd/tls.cert', 'rb').read()

# build ssl credentials using the cert the same as before
cert_creds = grpc.ssl_channel_credentials(cert)

# now build meta data credentials
auth_creds = grpc.metadata_call_credentials(metadata_callback)

# combine the cert credentials and the macaroon auth credentials
# such that every call is properly encrypted and authenticated
combined_creds = grpc.composite_channel_credentials(cert_creds, auth_creds)

# finally pass in the combined credentials when creating a channel
channel = grpc.secure_channel('10.21.21.9:10009', combined_creds)
stub = rpcstub.LightningStub(channel)

# now every call will be made with the macaroon already included


def get_info():
    info = stub.GetInfo(lnrpc.GetInfoRequest())
    return str(info)

def fee_report():
    request = lnrpc.FeeReportRequest()
    response = stub.FeeReport(request)
    return str(response)