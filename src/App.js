import './App.css';
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import MicroSocialFeed from './pages/feed';
import RegisterForm from './pages/signup';
import LoginForm from './pages/login';

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route path='/' element={<MicroSocialFeed />} />
        <Route path='/signup' element={<RegisterForm />} />
        <Route path='/login' element={<LoginForm />} />
      </>
    )
  );

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  );
}
export default App