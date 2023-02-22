# Sweet Treats
### Concept
Sweet Treats is an online site where user is able to order any customized dessert they want. Customers will be able to extensively describe how they want their dessert made, advise of allergies, and select their budget. 

### Technologies Used

* Django
* Bit.io
* Python
* React
* CSS

|Path|Action|
|----|----|
|'/'| Main |
|'/sweettreats/create'| Create|
|'/sweettreats/:id' | Show |
|'/sweettreats/update/:id' | Update |
|'/sweettreats/delete/:id' | Delete |

|Name|Data Type|
|----|----|
|id| Serial |
| Allergies | varchar(50)|
| Dessert Details | varchar(250) |
| Inspiration Link | TextField |
| Email | varchar(50)|
| Budget | varchar(6)|