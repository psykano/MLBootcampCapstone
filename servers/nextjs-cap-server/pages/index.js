import Head from "next/head";
import styles from "../styles/Home.module.css";
import React, { useState } from "react";
import Image from "next/image";
import Perfume from './perfume'

export default function Home() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [perfume, setPerfume] = useState(null)

  async function onSubmit(event) {
    event.preventDefault()
    setIsLoading(true)
    setError(null)
    setPerfume(null)

    try {
      const formData = new FormData(event.target)
      const body = {color: formData.get('color'), shape: formData.get('shape'), top: formData.get('top')}
      const response = await fetch('/api/prompt', {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
          'content-type': 'application/json'
        }
      })

      if (!response.ok) {
        throw new Error('Failed to submit the data.')
      }
   
      // Handle response if necessary
      const data = await response.json()
      if (data.image) {
        setPerfume(data.image)
      } else {
        throw new Error('Failed to generate perfume.')
      }
    } catch (error) {
      // Capture the error message to display to the user
      setError(error.message)
      console.error(error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Create Perfume</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <div className="mb-4">
          <h1 className={styles.title}>
            Create a new perfume
          </h1>
        </div>

        <div className="mb-8">
          <p className={styles.description}>
            Choose how you want your new perfume to look:
          </p>
        </div>

        <form className="bg-gray-50 shadow-md rounded px-8 pt-6 pb-8 mb-6" onSubmit={onSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="shape">
              Shape
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" name="shape" placeholder="Square" />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="bottlecolor">
              Bottle color
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" name="color" placeholder="Red" />
          </div>
            <div className="mb-6">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="topcolor">
              Top color
            </label>
            <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" name="top" placeholder="Silver" />
          </div>
          {isLoading ? (
            <button className="bg-gray-500 text-white font-bold py-2 px-4 rounded" type="submit" disabled>Submit</button>
          ) : (
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">Submit</button>
          )}
        </form>

        <Perfume isLoading={isLoading} error={error} perfume={perfume} />
      </main>

      <footer className={styles.footer}>
      </footer>
    </div>
  );
}
