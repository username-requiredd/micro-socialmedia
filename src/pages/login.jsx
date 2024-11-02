import React from "react";

const LoginForm = () => {
  return (
    <section className="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center px-6 py-8">
      <div className="w-full max-w-md bg-white rounded-lg shadow dark:bg-gray-800 dark:border dark:border-gray-700 p-6 space-y-6">
        <a href="#" className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
          <img className="w-8 h-8 mr-2" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" alt="logo" />
          Kojo
        </a>
        <h1 className="text-xl font-bold text-gray-900 md:text-2xl dark:text-white">
          Login to your account
        </h1>
        <form className="space-y-6" action="#">
          <div>
            <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email</label>
            <input type="email" name="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" placeholder="your email" required />
          </div>
          <div>
            <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
            <input type="password" name="password" id="password" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" placeholder="••••••••" required />
          </div>
          <button type="submit" className="w-full text-white bg-primary-600 hover:bg-primary-700 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700">Login</button>
          <p className="text-sm font-light text-gray-500 dark:text-gray-400">
            Don’t have an account? <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">Sign up here</a>
          </p>
        </form>
      </div>
    </section>
  );
};

export default LoginForm;
