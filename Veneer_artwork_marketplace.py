#-----------Classes------------
class Marketplace:
  def __init__(self):
    self.listing = []
  #methods to remove or add an artwork to the market's listing of artworks
  def add_listing(self, new_listing):
    self.listing.append(new_listing)

  def remove_listing(self, artwork):
    for i in range(len(self.listing)):
      if self.listing[i].art==artwork: 
        self.listing.pop(i)

  #method to show what's available on the market
  def show_listing(self):
    for i in range(len(self.listing)):
      print(self.listing[i])
      

class Art:
  def __init__(self, artist, title, year, medium, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return "{artist}. \"{title}\". {year}, {medium}. {owner}, {location}".format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location) 


class Client:
  def __init__(self, name, location, is_museum, wallet):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    self.wallet = wallet

  #methods to buy/sell an artwork
  def sell_artwork(self, artwork, price, currency):
    if self == artwork.owner:
        listing = Listing(artwork, price, currency, artwork.owner)
        veneer.add_listing(listing)
    else: print("You're not the owner of this artwork.")
  
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      if self.wallet>=artwork.price:
        if artwork in veneer.listing: 
          self.remove_funds(price)
          art_listing = artwork
          artwork.owner = self
          veneer.remove_listing(artwork)
        else: 
          print("The artwork you're searching for is not listed in the marketplace.")
          return
      else: print("You do not have enough funds in your wallet.")
    else: print("You cannot buy your own artworks.")

  # methods to control wallet
  def add_funds(self, amount):
    self.wallet += amount
  
  def remove_funds(self, amount):
    if self.wallet >= amount: 
      self.wallet -= amount
    else: 
      print("Error: not enough funds.")


# class to list the artworks on the marketplace
class Listing:
  def __init__(self, art, price, currency, seller):
    self.art = art
    self.price = price
    self.currency = currency
    self.seller = seller
  
  def __repr__(self):
    return "{name}, {price}{currency}".format(name=self.art.title, price=self.price, currency=self.currency)

  

  
#-----------Code/Tests-----------
veneer = Marketplace()
veneer.show_listing()

moma = Client("The MOMA", "New York", True, 5000000)
edytta = Client("Edytta Halpirt", "Private collection", False, 1000000)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)


edytta.sell_artwork(girl_with_mandolin, 6000000, "USD")

print(edytta.wallet)

veneer.show_listing()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

veneer.show_listing()
