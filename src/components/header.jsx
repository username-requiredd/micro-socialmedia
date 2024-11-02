import React from "react";
import { Bell, Search, User } from "lucide-react";

const Header = () => {
  return (
    <header className="bg-white dark:bg-gray-800 shadow-sm">
      <div className="w-full md:mx-auto px-4 py-3 flex items-center justify-between">
        {/* Logo */}
        <a href="#" className="text-2xl font-semibold text-gray-900 dark:text-white flex items-center">
          <img
            className="w-8 h-8 mr-2"
            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg"
            alt="logo"
          />
         Kojo
        </a>

        {/* Search Bar */}
        <div className=" hidden flex-1 mx-4">
          <div className="relative w-full">
            <input
              type="text"
              placeholder="Search..."
              className="w-1/2 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 p-2 pl-10 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
            />
            <Search className="absolute left-3 top-2.5 h-4 w-4 text-gray-500 dark:text-gray-300" />
          </div>
        </div>

        {/* Notification and Profile Icons */}
        <div className="flex items-center space-x-4">
          <button className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700">
            <Bell className="h-5 w-5 text-gray-700 dark:text-gray-300" />
          </button>
          <button className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700">
            <User className="h-5 w-5 text-gray-700 dark:text-gray-300" />
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;
