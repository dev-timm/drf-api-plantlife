# PlantLife DRF API

The PlantLife DRF API is the backend solution for the PlantLife React App. 
The API is built upon Django while Cloudinary is used to host images.

[Link to the project](https://drf-api-plantlife-bdbe99797603.herokuapp.com/)

## Database
![An image of the hero section](assets/readme/models.png)

The database consists of 9 models. 
The User model is directly related to the Profile, Follower, Advertisement, Bookmark and Post model. Subsequently the Post model further passes down information to the Report, Like and Comment model.
