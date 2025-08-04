1.Display the Active Admin User
Currently, the system does not indicate which admin user is currently logged in.
This makes it difficult to track who performed specific actions for testing purposes, especially parking events.

Suggested Improvement:
Add clear UI elements that display the active user’s identity (e.g., in the header or sidebar), and record the user in the parking logs.

2.Modernize the Architecture
The system currently uses full-page reloads and does not communicate via separate API calls.

Suggested Improvements:
Migrate to a Single Page Application (SPA) architecture or at least decouple frontend and backend using a RESTful API layer.
Use AJAX/Fetch for dynamic interactions and return JSON responses for better performance and testability.
Add Swagger (OpenAPI) documentation to define and test endpoints easily.

3.Improve Session & Authentication
Current State:
The system appears to rely on traditional session cookies for login tracking.
Suggested Improvement:
Move to token-based authentication (e.g., JWT) to simplify API testing and enhance security across sessions.


4.Live Reports and Statistics
Suggested Feature:
Enable real-time dashboards and usage reports using WebSocket or polling mechanisms.
This would allow monitoring parking activity and system status live.

5.Additional Functional Observations
Language Consistency:
Parts of the system interface are in Hebrew and others in English. A consistent language should be applied throughout the system.

6.Slot Input Validation:
The slot input field currently accepts any character, including non-numeric and invalid symbols.
It should be restricted to valid slot identifiers only.

7.History Limitations:
The system currently shows only the last 48 history records and does not support deletion.
This limits traceability and usability for larger parking lots.

8.File Upload Restrictions:
The system should prevent uploading unsupported image formats and potentially malicious files.
Consider adding file type validation and antivirus scanning for uploads.
Right now I can add a non image formats

📝 Final Note:
After analyzing network traffic, I found that the system relies entirely on full page loads rather than API or AJAX calls. Therefore, I focused on thorough UI testing using Selenium to validate interface behavior and logic through the browser.