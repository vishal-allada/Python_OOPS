class Apple:   # Base class
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to",self.contactWebsite)

class MacBook(Apple): # Derived class
    def __init__(self):
        self.yearOfManufacturer = 2017
    
    def manufacturerDetails(self):
        print("The Macbook was manufactured in the year {} by {}".format(self.yearOfManufacturer,self.manufacturer))

macbook = MacBook()
macbook.manufacturerDetails()
macbook.contactDetails()