export default function handler(req, res) {
    // Check if the Authorization header contains the correct token
    if (req.headers.authorization !== `Bearer ${process.env.CRON_SECRET}`) {
      // If not authorized, return a 401 Unauthorized response
      return res.status(401).end('Unauthorized');
    }
  
    // If authorized, continue with the cron job logic
    // For demonstration purposes, let's just log a message and send a success response
    console.log('Cron job executed successfully');
    res.status(200).end('Cron job executed successfully');
  }
  