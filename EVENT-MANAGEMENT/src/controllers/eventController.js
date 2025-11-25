const Event = require('../models/Event');

// 1. Create Event
exports.createEvent = async (req, res) => {
  try {
    const event = new Event({
      ...req.body,
      organizer: req.user._id // Associate event with logged-in user
    });
    await event.save();
    res.status(201).json(event);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

// 2. Get All Events (with Filter)
exports.getEvents = async (req, res) => {
  try {
    const { date, location } = req.query;
    const query = { status: 'approved' }; // Only show approved events to public

    if (date) query.date = new Date(date);
    if (location) query.location = { $regex: location, $options: 'i' }; // Case insensitive search

    const events = await Event.find(query).populate('organizer', 'username');
    res.json(events);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// 3. Register for Event (Capacity Logic)
exports.registerEvent = async (req, res) => {
  try {
    const event = await Event.findById(req.params.id);
    
    if (!event) return res.status(404).json({ message: 'Event not found' });
    if (event.status !== 'approved') return res.status(400).json({ message: 'Event not approved yet' });
    
    // Check Capacity
    if (event.attendees.length >= event.capacity) {
      return res.status(400).json({ message: 'Event is fully booked' });
    }

    // Check if already registered
    if (event.attendees.includes(req.user._id)) {
      return res.status(400).json({ message: 'You are already registered' });
    }

    event.attendees.push(req.user._id);
    await event.save();
    
    res.json({ message: 'Registration successful' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// 4. Cancel Registration
exports.cancelRegistration = async (req, res) => {
  try {
    const event = await Event.findById(req.params.id);
    if (!event) return res.status(404).json({ message: 'Event not found' });

    event.attendees = event.attendees.filter(
      (userId) => userId.toString() !== req.user._id.toString()
    );
    
    await event.save();
    res.json({ message: 'Registration cancelled' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// 5. Approve Event (Admin Only)
exports.approveEvent = async (req, res) => {
  try {
    const event = await Event.findById(req.params.id);
    if (!event) return res.status(404).json({ message: 'Event not found' });

    event.status = 'approved';
    await event.save();
    res.json({ message: 'Event approved', event });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};