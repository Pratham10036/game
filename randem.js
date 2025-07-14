// Utility Functions Collection

// Generate a random number between min and max (inclusive)
const randomNumber = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1) + min);
};

// Shuffle an array using Fisher-Yates algorithm
const shuffleArray = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
};

// Generate a random color in hexadecimal format
const randomColor = () => {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
};

// Check if a string is a palindrome
const isPalindrome = (str) => {
  const cleanStr = str.toLowerCase().replace(/[^a-z0-9]/g, "");
  return cleanStr === cleanStr.split("").reverse().join("");
};

// Generate a random password
const generatePassword = (length = 12) => {
  const charset =
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+";
  return Array.from(
    { length },
    () => charset[Math.floor(Math.random() * charset.length)]
  ).join("");
};

// Deep clone an object
const deepClone = (obj) => {
  if (obj === null || typeof obj !== "object") return obj;
  if (Array.isArray(obj)) return obj.map(deepClone);
  return Object.fromEntries(
    Object.entries(obj).map(([key, value]) => [key, deepClone(value)])
  );
};

// Debounce function
const debounce = (func, delay) => {
  let timeoutId;
  return function (...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
};

// Format number with commas
const formatNumber = (num) => {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};

// Calculate time difference in a human-readable format
const getTimeDifference = (date1, date2) => {
  const diff = Math.abs(date2 - date1);
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  return `${days}d ${hours}h ${minutes}m`;
};

// Sample data structure for testing
const sampleData = {
  users: [
    { id: 1, name: "John Doe", age: 30, email: "john@example.com" },
    { id: 2, name: "Jane Smith", age: 25, email: "jane@example.com" },
    { id: 3, name: "Bob Johnson", age: 35, email: "bob@example.com" },
  ],
  products: [
    { id: 1, name: "Laptop", price: 999.99, stock: 50 },
    { id: 2, name: "Smartphone", price: 499.99, stock: 100 },
    { id: 3, name: "Headphones", price: 99.99, stock: 200 },
  ],
};

// Example usage and testing
console.log("Random number between 1 and 10:", randomNumber(1, 10));
console.log("Random color:", randomColor());
console.log('Is "racecar" a palindrome?', isPalindrome("racecar"));
console.log("Random password:", generatePassword());
console.log("Formatted number:", formatNumber(1234567.89));

// Test array operations
const numbers = [1, 2, 3, 4, 5];
console.log("Shuffled array:", shuffleArray([...numbers]));

// Test object operations
const clonedData = deepClone(sampleData);
console.log("Cloned data structure:", clonedData);

// Test time difference
const date1 = new Date("2023-01-01");
const date2 = new Date("2023-01-03 12:30");
console.log("Time difference:", getTimeDifference(date1, date2));

// Example of debounced function
const debouncedSearch = debounce((searchTerm) => {
  console.log("Searching for:", searchTerm);
}, 500);

// Simulate search input
debouncedSearch("hello");
debouncedSearch("hello w");
debouncedSearch("hello world"); // Only this one will execute after 500ms
