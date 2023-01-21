import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext';
import { Login } from './components/Auth/Login';
import { PublicRoute } from './components/Auth/PublicRoute';
import { Register } from './components/Auth/Register';
import { NavBar } from './components/Navbar/NavBar';
import { Authenticated } from './components/Auth/Authenticated';
import { NotesList } from './components/Notes/NotesList';
import { NoteDetail } from './components/Notes/NoteDetail';

function App() {
  return (
    <div className="App">
      <Router>
        <AuthProvider>
          <Routes>
            <Route path="/" element={<NavBar />}>
              <Route path="/login" element={<PublicRoute><Login /></PublicRoute>} />
              <Route path="/register" element={<PublicRoute><Register /></PublicRoute>} />
              <Route path="/" element={<Authenticated><NotesList /></Authenticated>} />
              <Route path="/:noteId" element={<Authenticated><NoteDetail /></Authenticated>} />
            </Route>
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
