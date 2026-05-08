import { useState, useEffect } from "react"
import { Link, useLocation } from "react-router-dom"
import { motion, AnimatePresence } from "motion/react"
import { Menu, X } from "lucide-react"

const links = [
  { to: "/", label: "Home" },
  { to: "/about", label: "About" },
  { to: "/programs", label: "Programs" },
  { to: "/how-it-works", label: "How It Works" },
  { to: "/for-schools", label: "For Schools" },
]

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const { pathname } = useLocation()

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20)
    window.addEventListener("scroll", onScroll)
    return () => window.removeEventListener("scroll", onScroll)
  }, [])

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? "bg-white/95 backdrop-blur-sm shadow-sm" : "bg-transparent"
      }`}
    >
      <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-[#f97316] flex items-center justify-center shadow-md rotate-3">
            <span className="text-white font-black text-xl" style={{ fontFamily: "Nunito, sans-serif" }}>F</span>
          </div>
          <div>
            <span className="font-black text-xl text-gray-900 leading-none" style={{ fontFamily: "Nunito, sans-serif" }}>
              Find Your Voice
            </span>
            <p className="text-[10px] text-[#f97316] font-bold uppercase tracking-widest leading-none mt-0.5">
              Youth Academy
            </p>
          </div>
        </Link>

        <div className="hidden md:flex items-center gap-1">
          {links.map((link) => (
            <Link
              key={link.to}
              to={link.to}
              className={`text-sm font-bold transition-colors px-3 py-1.5 rounded-lg relative ${
                pathname === link.to
                  ? "text-gray-900"
                  : "text-gray-500 hover:text-gray-900"
              }`}
              style={{ fontFamily: "Nunito, sans-serif" }}
            >
              {link.label}
              {pathname === link.to && (
                <motion.div
                  layoutId="nav-indicator"
                  className="absolute -bottom-0.5 left-2 right-2 h-[3px] bg-[#f97316] rounded-full"
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                />
              )}
            </Link>
          ))}
          <Link to="/contact" className="ml-3">
            <motion.button
              className="bg-[#f97316] text-white px-5 py-2 rounded-full text-sm font-black shadow-md shadow-orange-200 hover:bg-[#ea580c] transition-colors"
              style={{ fontFamily: "Nunito, sans-serif" }}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              Enroll Now
            </motion.button>
          </Link>
        </div>

        <button
          className="md:hidden text-gray-700 w-10 h-10 flex items-center justify-center rounded-xl hover:bg-gray-100"
          onClick={() => setOpen(!open)}
        >
          {open ? <X size={22} /> : <Menu size={22} />}
        </button>
      </div>

      <AnimatePresence>
        {open && (
          <motion.div
            key="mobile-menu"
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden bg-white border-t border-gray-100 overflow-hidden"
          >
            <div className="px-6 py-5 flex flex-col gap-2">
              {links.map((link) => (
                <Link
                  key={link.to}
                  to={link.to}
                  onClick={() => setOpen(false)}
                  className={`text-base font-bold py-2.5 px-4 rounded-xl ${
                    pathname === link.to
                      ? "bg-[#fff7ed] text-[#f97316]"
                      : "text-gray-600"
                  }`}
                  style={{ fontFamily: "Nunito, sans-serif" }}
                >
                  {link.label}
                </Link>
              ))}
              <Link
                to="/contact"
                onClick={() => setOpen(false)}
                className="bg-[#f97316] text-white px-6 py-3 rounded-full text-base font-black text-center mt-2 shadow-md shadow-orange-200"
                style={{ fontFamily: "Nunito, sans-serif" }}
              >
                Enroll Now
              </Link>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  )
}
