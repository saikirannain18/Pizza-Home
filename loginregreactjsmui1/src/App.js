import { BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import LoginReg from "./pages/auth/LoginReg";
import ResetPassword from "./pages/auth/ResetPassword";
import SendPasswordResetEmail from "./pages/auth/SendPasswordResetEmail";
// import Contact from "./pages/Menu";
import Dashboard from "./pages/Dashboard";
import Home from "./pages/Home";
import Menu from './pages/Menu';
import Menu1 from './pages/Menu1';
import About from './pages/About';
import Footer from './components/Footer';
import Layout from "./pages/Layout";
import { useSelector } from "react-redux";

function App() {
  const { access_token } = useSelector(state => state.auth)
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="/about" element={<About/>}/>
            <Route path="/menu" element={<Menu/>}/>
            <Route path="/menu1" element={<Menu1/>}/>
            {/* <Route path="contact" element={<Contact />} /> */}
            <Route path="login" element={!access_token ? <LoginReg /> : <Navigate to="/dashboard" />} />
            <Route path="sendpasswordresetemail" element={<SendPasswordResetEmail />} />
            <Route path="api/user/reset/:id/:token" element={<ResetPassword />} />
          </Route>
          <Route path="/dashboard" element={access_token ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="*" element={<h1>Error 404 Page not found !!</h1>} />
        </Routes>
        <Footer/>
      </BrowserRouter>
    </>
  );
}

export default App;
