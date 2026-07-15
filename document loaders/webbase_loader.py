from langchain_community.document_loaders import WebBaseLoader

url='https://www.squarespace.com/go/create-a-website?channel=pnb&subchannel=go&campaign=pnb-go-in-multi-core_website-mix&subcampaign=(general-en_webpage_e)&channel=pnb&subchannel=go&campaign=23803337437&subcampaign=196705557515_kwd-16034750_e&source=&gclsrc=aw.ds&gad_source=1&gad_campaignid=23803337437&gbraid=0AAAAADxS_FJRVjGlgv-_xG6n0H_jpG0Ht&gclid=CjwKCAjwvNfSBhBiEiwAyaGMCZvbWaW8lsM17MgroPjGvnaF9VQ-AbsmwUCJut4r1Wmcjwkjt1w95BoC3dkQAvD_BwE'

loader=WebBaseLoader(url)

doc=loader.load()

print(doc[0].page_content)

print(doc)
