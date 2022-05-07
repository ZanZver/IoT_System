require("./models/db"); //reguire DB connection

const express = require("express");
const path = require("path");
const exphbs = require("express-handlebars");
const bodyparser = require("body-parser");

const employeeController = require("./controllers/employeeController");
const homeController = require("./controllers/homeController");
const forgotPasswordController = require("./controllers/forgotPasswordController");
const registerController = require("./controllers/registerController");
const lightsController = require("./controllers/lightsController");
const fridgeController = require("./controllers/fridgeController");
const vacuumController = require("./controllers/vacuumController");

var app = express();
app.use(bodyparser.urlencoded({
    extended: true
}));

app.set("views", path.join(__dirname, "/views/"));
app.engine('hbs', exphbs.engine({ extname: 'hbs', defaultLayout: 'mainLayout', layoutsDir: __dirname + '/views/layouts/' }));
app.set("view engine", "hbs");

app.listen(3000, () => {
    console.log("Express server started at port: 3000");
})

app.use("/employee", employeeController); //routs to employeeController 
app.use("/home", homeController); //routs to employeeController
app.use("/forgotPassword", forgotPasswordController); //routs to employeeController
app.use("/register", registerController); //routs to employeeController
app.use("/devices/smart_light", lightsController);
app.use("/devices/smart_fridge", fridgeController);
app.use("/devices/smart_vacuum", vacuumController);