// src/routes/eventRoutes.js

const express = require('express');
const router = express.Router();
const { 
  createEvent, 
  getEvents, 
  approveEvent // Keep these functions from eventController
} = require('../controllers/eventController'); 
const { // <-- NEW: Import booking logic from the new controller
  registerEvent, 
  cancelRegistration 
} = require('../controllers/bookingController');
const { protect, admin } = require('../middleware/authMiddleware');

// ... (Rest of the code remains the same) ...

// Protected Routes
router.post('/', protect, createEvent);
router.post('/:id/register', protect, registerEvent);  // <-- Uses new controller
router.delete('/:id/register', protect, cancelRegistration); // <-- Uses new controller

// ...
module.exports = router;