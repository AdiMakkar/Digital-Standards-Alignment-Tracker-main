// Download GoLang on your device and add packages
// Check the go version in your terminal
go version

// assetfinder is used to find the websites
sudo go install github.com/tomnomnom/assetfinder@latest
// Device will prompt you enter your password

// Declare your PATHS
export GOPATH=$HOME/go
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

// assetfinder search in terminal 
assetfinder - h
// assetfidner retunrs all the domains with gc.ca
assetfinder gc.ca