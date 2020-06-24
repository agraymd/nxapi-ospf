import requests

'''

Hardware Used: cisco Nexus9000 C9372PX chassis 
Code Version : NXOS: version 9.3(4)


+ Authentication Section on box 1

  Sets authenticate_url to url needed to authenticate with NX-API 
  Sets the headers and payload to required values
  Uses requests library to post to the box, and stores the response in variable 'response'
  Stores the token by using requests library to grab it from a cookie in response 'APIC-cookie'
  
  NOTE: Items that need your input are designated with !!! CHANGE ME !!! placeholders. 
  
  You need to replace the IP address / URL of your box, and the username and password portions of the authenticate_payload

'''

# Starts authentication section on box 1
authenticate_url = "http://!!! CHANGE ME !!!/api/aaaLogin.json"

authenticate_headers = {
  'Content-Type': 'application/json',
  }

authenticate_payload = "{\"aaaUser\": {\"attributes\": {\"name\": \"!!! CHANGE ME !!!\", \"pwd\": \"!!! CHANGE ME !!!\"}}}"

response = requests.post(authenticate_url, headers=authenticate_headers, data=authenticate_payload)

# Stores the token in variable token for use later 
token = response.cookies['APIC-cookie']


'''

+ Starts interface and OSPF Config on box 1

  NOTE: Items that need your input are designated with !!! CHANGE ME !!! placeholders. 
  
  You need to replace the IP address / URL of your box.
  
  Also note that you may want to change the payload. This is set to run the following commands: 
  
        feature ospf 
        router ospf API-MADE
        router-id 1.1.1.1
        exit
        int e1/1
        no switchport 
        ip address 1.1.1.1/30
        ip router ospf API-MADE area 0
        no shut
    
    You can either look through the json to change it for your needs, or use the nx-api sandbox to generate your own payload.

'''


ospf_url = "http://!!! CHANGE ME !!!/api/mo/sys.json"

ospf_payload = "{\r\n  \"topSystem\": {\r\n    \"attributes\": {\r\n      \"dn\": \"sys\",\r\n      \"rn\": \"sys\"\r\n    },\r\n    \"children\": [\r\n      {\r\n        \"ipv4Entity\": {\r\n          \"attributes\": {\r\n            \"dn\": \"sys/ipv4\",\r\n            \"rn\": \"ipv4\"\r\n          },\r\n          \"children\": [\r\n            {\r\n              \"ipv4Inst\": {\r\n                \"attributes\": {\r\n                  \"dn\": \"sys/ipv4/inst\",\r\n                  \"rn\": \"inst\"\r\n                },\r\n                \"children\": [\r\n                  {\r\n                    \"ipv4Dom\": {\r\n                      \"attributes\": {\r\n                        \"dn\": \"sys/ipv4/inst/dom-default\",\r\n                        \"name\": \"default\",\r\n                        \"rn\": \"dom-default\"\r\n                      },\r\n                      \"children\": [\r\n                        {\r\n                          \"ipv4If\": {\r\n                            \"attributes\": {\r\n                              \"dn\": \"sys/ipv4/inst/dom-default/if-[eth1/1]\",\r\n                              \"id\": \"eth1/1\",\r\n                              \"rn\": \"if-[eth1/1]\"\r\n                            },\r\n                            \"children\": [\r\n                              {\r\n                                \"ipv4Addr\": {\r\n                                  \"attributes\": {\r\n                                    \"addr\": \"1.1.1.1/30\",\r\n                                    \"dn\": \"sys/ipv4/inst/dom-default/if-[eth1/1]/addr-[1.1.1.1/30]\",\r\n                                    \"pref\": \"0\",\r\n                                    \"rn\": \"addr-[1.1.1.1/30]\",\r\n                                    \"tag\": \"0\"\r\n                                  }\r\n                                }\r\n                              }\r\n                            ]\r\n                          }\r\n                        }\r\n                      ]\r\n                    }\r\n                  }\r\n                ]\r\n              }\r\n            }\r\n          ]\r\n        }\r\n      },\r\n      {\r\n        \"interfaceEntity\": {\r\n          \"attributes\": {\r\n            \"dn\": \"sys/intf\",\r\n            \"rn\": \"intf\"\r\n          },\r\n          \"children\": [\r\n            {\r\n              \"l1PhysIf\": {\r\n                \"attributes\": {\r\n                  \"adminSt\": \"up\",\r\n                  \"dn\": \"sys/intf/phys-[eth1/1]\",\r\n                  \"id\": \"eth1/1\",\r\n                  \"layer\": \"Layer3\",\r\n                  \"rn\": \"phys-[eth1/1]\",\r\n                  \"userCfgdFlags\": \"admin_layer,admin_state\"\r\n                }\r\n              }\r\n            }\r\n          ]\r\n        }\r\n      },\r\n      {\r\n        \"ospfEntity\": {\r\n          \"attributes\": {\r\n            \"dn\": \"sys/ospf\",\r\n            \"rn\": \"ospf\"\r\n          },\r\n          \"children\": [\r\n            {\r\n              \"ospfInst\": {\r\n                \"attributes\": {\r\n                  \"dn\": \"sys/ospf/inst-API-CONFIG\",\r\n                  \"name\": \"API-CONFIG\",\r\n                  \"rn\": \"inst-API-CONFIG\"\r\n                },\r\n                \"children\": [\r\n                  {\r\n                    \"ospfDom\": {\r\n                      \"attributes\": {\r\n                        \"dn\": \"sys/ospf/inst-API-CONFIG/dom-default\",\r\n                        \"name\": \"default\",\r\n                        \"rn\": \"dom-default\"\r\n                      },\r\n                      \"children\": [\r\n                        {\r\n                          \"ospfIf\": {\r\n                            \"attributes\": {\r\n                              \"advertiseSecondaries\": \"yes\",\r\n                              \"area\": \"0.0.0.0\",\r\n                              \"dn\": \"sys/ospf/inst-API-CONFIG/dom-default/if-[eth1/1]\",\r\n                              \"id\": \"eth1/1\",\r\n                              \"rn\": \"if-[eth1/1]\"\r\n                            }\r\n                          }\r\n                        }\r\n                      ]\r\n                    }\r\n                  }\r\n                ]\r\n              }\r\n            },\r\n            {\r\n              \"ospfInst\": {\r\n                \"attributes\": {\r\n                  \"dn\": \"sys/ospf/inst-API-MADE\",\r\n                  \"name\": \"API-MADE\",\r\n                  \"rn\": \"inst-API-MADE\"\r\n                },\r\n                \"children\": [\r\n                  {\r\n                    \"ospfDom\": {\r\n                      \"attributes\": {\r\n                        \"dn\": \"sys/ospf/inst-API-MADE/dom-default\",\r\n                        \"name\": \"default\",\r\n                        \"rn\": \"dom-default\",\r\n                        \"rtrId\": \"1.1.1.1\"\r\n                      }\r\n                    }\r\n                  }\r\n                ]\r\n              }\r\n            }\r\n          ]\r\n        }\r\n      },\r\n      {\r\n        \"fmEntity\": {\r\n          \"attributes\": {\r\n            \"dn\": \"sys/fm\",\r\n            \"rn\": \"fm\"\r\n          },\r\n          \"children\": [\r\n            {\r\n              \"fmOspf\": {\r\n                \"attributes\": {\r\n                  \"adminSt\": \"enabled\",\r\n                  \"dn\": \"sys/fm/ospf\",\r\n                  \"rn\": \"ospf\"\r\n                }\r\n              }\r\n            }\r\n          ]\r\n        }\r\n      }\r\n    ]\r\n  }\r\n}"
ospf_headers = {
  'Content-Type': 'application/json',
  'Cookie': ''
}

# Set value of Cookie key in ospf_headers to token
ospf_headers['Cookie'] = "APIC-cookie=" + token

response = requests.request("POST", ospf_url, headers=ospf_headers, data = ospf_payload)

print(response.text.encode('utf8'))