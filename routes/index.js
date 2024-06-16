const express = require("express");
const router = express.Router();
const indexController = require("../controllers/indexController");

// router.get('/', indexController.getIndex);
router.post("/verifier-url", indexController.postUrl);

module.exports = router;
