/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*"],
  theme: {
    extend: {
      backgroundImage: {
         pic1: "url(./assets/BG.png)",
      }
    },
    fontFamily: {
      heading: ['Poppins', 'sans-serif'],
      para: ['Bai jamjuree', 'sans-serif']
    }
  },
  plugins: [],
}
