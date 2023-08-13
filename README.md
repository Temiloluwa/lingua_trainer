# lingua_trainer

An Assistant for Language Learning


## Endpoints


1. **User Authentication and Authorization:**
   - `/api/register` (POST): Register a new user account.
   - `/api/login` (POST): Authenticate and log in a user.
   - `/api/logout` (POST): Log out the currently authenticated user.
   - `/api/user/profile` (GET, PUT): Get or update user profile information.

2. **Word and Phrase Management:**
   - `/api/words` (GET, POST): Get a list of uploaded words and phrases or upload new ones.
   - `/api/words/:id` (GET, PUT, DELETE): Get, update, or delete a specific word/phrase by ID.

3. **Challenge Generation:**
   - `/api/challenges` (GET): Generate a list of challenges based on uploaded words and phrases.

4. **Challenge Submission:**
   - `/api/challenges/:id/submit` (POST): Submit a user's answer to a challenge for evaluation.

5. **Challenge History:**
   - `/api/user/challenges` (GET): Get a user's challenge history and results.

6. **Leaderboard and Statistics:**
   - `/api/leaderboard` (GET): Get a list of top users based on challenge performance.
   - `/api/user/statistics` (GET): Get user-specific language learning statistics.

7. **User Data Management:**
   - `/api/user/words` (GET, POST): Get a user's uploaded words and phrases or upload new ones.
   - `/api/user/words/:id` (GET, PUT, DELETE): Get, update, or delete a specific user-uploaded word/phrase.

8. **Feedback and Support:**
   - `/api/feedback` (POST): Allow users to provide feedback or support requests.
