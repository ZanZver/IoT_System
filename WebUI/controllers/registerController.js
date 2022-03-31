//.lean()
const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const User = mongoose.model('User');
const Employee = mongoose.model('Employee');

router.get('/', (req, res) => {
    res.render("employee/registerPage", {
        viewTitle: "Register"
    }); //what hbs you want to render
});

router.post('/', (req, res) => {
    if (req.body._id == '')
        insertRecord(req, res);
        else
        updateRecord(req, res);
});

function insertRecord(req, res) {
    var user = new User();
    user.username = req.body.username;
    user.email = req.body.email;
    user.password = req.body.password;
    user.name = req.body.name;
    user.surname = req.body.surname;
    //user.addressLine1 = req.body.addressLine1;
    //user.addressLine2 = req.body.addressLine2;
    user.address = [req.body.addressLine1,req.body.addressLine2]
    //
    user.postcode = req.body.postcode;
    user.city = req.body.city;
    user.country = req.body.country;
    console.log("User info");
    console.log(req.body);
    user.save((err, doc) => {
        if (!err){  
            console.log("Here 2");
            res.redirect('/home');
        }
        else {
            if (err.name == 'ValidationError') {
                handleValidationError(err, req.body);
                res.render("employee/homePage", {
                    viewTitle: "Home",
                    user: req.body
                });
            }
            else
                console.log('Error during record insertion : ' + err);
        }
    });
}

router.get('/forgotPassword', (req, res) => {
    Employee.find((err, docs) => {
        if (!err) {
            res.render("/forgotPassword", {
                list: docs
            });
        }
        else {
            console.log('Error in retrieving employee list :' + err);
        }
    }).lean();
});


function handleValidationError(err, body) {
    for (field in err.errors) {
        switch (err.errors[field].path) {
            case 'fullName':
                body['fullNameError'] = err.errors[field].message;
                break;
            case 'fullName2':
                    body['fullNameError'] = err.errors[field].message;
                    break;
            case 'email':
                body['emailError'] = err.errors[field].message;
                break;
            default:
                break;
        }
    }
}

router.get('/:id', (req, res) => {
    Employee.findById(req.params.id, (err, doc) => {
        if (!err) {
            res.render("employee/addOrEdit", {
                viewTitle: "Update Employee",
                employee: doc
            });
        }
    }).lean();
});

module.exports = router;