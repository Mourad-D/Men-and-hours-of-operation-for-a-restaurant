class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.frnachises = franchises
  



class Franchise:
  
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus 
    
  def __repr__(self):
    return "Lucky you Reston Residents !! Our New location is located @ "+self.address +'.\nWhat are you thinking now ?'
  
  def available_menus(self,time):
    available_menu = []
    for menu in self.menus:
      if menu.start_time >= time <= menu.end_time:
        available_menu.append(menu)
    return available_menu
  
class Menu:
  
  def __init__(self,name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
     return self.name + ' available from {0} to {1}'.format(self.start_time,self.end_time)
  

  def calculate_bill(self,purchased_items): 
    bill = 0
    for item in purchased_items :
      #if item in self.items:
        bill += self.items[item]
    return bill




brunch_menu_elements = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice':3.50,
}

early_bird_menu_elements= {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_menu_elements = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_menu_elements = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00,
}

#new_business_menu_elements 
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
brunch = Menu("brunch",brunch_menu_elements,1100,1600)

early_bird = Menu("early_bird",early_bird_menu_elements,1500,1800)

dinner = Menu("dinner",dinner_menu_elements,1700,2300)

kids = Menu('kids',kids_menu_elements,1100,2100)

arepas_menu =Menu('arepas',arepas_menu,1000,2000)

menus = [dinner, early_bird, brunch, kids,arepas_menu]



flagship_store =Franchise("1232 West End Road",menus)

new_installment =Franchise("12 East MulberryStreet",menus)

b1 = Business('Basta Fazoolin with my Heart',[new_installment,flagship_store])

arepas = Franchise("189 Fitzgerald Avenue", menus)

b2 = Business("Take a Arepa",[new_installment,flagship_store,arepas])
              


print(*arepas.available_menus(1200))

#print(flagship_store.available_menus(1000))