import { Routes, Route } from "react-router-dom"
import { useEffect } from "react"
import { useLocation } from "react-router-dom"
import Navbar from "./components/Navbar"
import Footer from "./components/Footer"
import Home from "./pages/Home"
import About from "./pages/About"
import Programs from "./pages/Programs"
import HowItWorks from "./pages/HowItWorks"
import ForSchools from "./pages/ForSchools"
import Contact from "./pages/Contact"

function ScrollToTop() {
  const { pathname } = useLocation()
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [pathname])
  return null
}

function App() {
  return (
    <div className="min-h-screen bg-white">
      <ScrollToTop />
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/programs" element={<Programs />} />
        <Route path="/how-it-works" element={<HowItWorks />} />
        <Route path="/for-schools" element={<ForSchools />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
      <Footer />
    </div>
  )
}

export default App
