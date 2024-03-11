const CELCIUS_TO_KELVIN = 273.15
const CELCIOUs_TO_FARHENITE = 32

function convertTemperature(celcius) {
    let celcius_to_kelvin = celcius + CELCIUS_TO_KELVIN
    let celcius_to_farhaneiet = celcius * 1.8 + CELCIOUs_TO_FARHENITE
    return [formattedTemp(celcius_to_kelvin), formattedTemp(celcius_to_farhaneiet)]
}

function formattedTemp(value) {
    return Number(value.toFixed(5))   
}

console.log(convertTemperature(36.50))