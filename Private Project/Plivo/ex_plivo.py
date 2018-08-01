import plivo

client = plivo.RestClient(auth_id='YOUR_AUTH', auth_token='YOUR_TOKEN')

response = client.messages.create(
    src='1111111111',
    dst='+821012345678',
    text='Hello?'
)

# Prints the complete response
print(response)