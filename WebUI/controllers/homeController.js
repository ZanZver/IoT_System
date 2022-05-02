//.lean()
const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const User = mongoose.model('User');
const Employee = mongoose.model('Employee');
const IoT_Customer_Device = mongoose.model("IoT_Customer_Device");

router.get('/', (req, res) => {
    res.render("employee/homePage", {
        viewTitle: "User login"
    }); //what hbs you want to render
});

router.post('/', (req, res) => {
    if (req.body._id == '')
        insertRecord(req, res);
        else
        updateRecord(req, res);
});

function insertRecord(req, res) {
    var userKeyID = "626f01d0574b1a1c1b8d2086";

    IoT_Customer_Device.aggregate([
        {$match: {UserID:userKeyID}},
        {$unwind: "$Devices"
        },
        {$project: {
            "smart_light" : "$Devices.smart_light",
            "smart_fridge" : "$Devices.smart_fridge",
            "smart_vacuum" : "$Devices.smart_vacuum",
            "_id": 0
        }}
    ]).exec((err, docs) => {
        if (!err) {
            console.log(docs);
            //console.log(res.json(docs));
            res.render("employee/userPage", {
                list: docs[0]
            });
        }
        else {
            console.log('Error in retrieving employee list :' + err);
        }
    })
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