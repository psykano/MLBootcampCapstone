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

      console.log('here:')
      console.log(formData.get('shape'))

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
        <h1 className={styles.title}>
          Create a new perfume
        </h1>

        <p className={styles.description}>
          Choose how you want your new perfume to look:
        </p>

        <form onSubmit={onSubmit}>
          <p>Shape:</p>
          <input type="text" name="shape" placeholder="Square" />
          <p>Bottle color:</p>
          <input type="text" name="color" placeholder="Red" />
          <p>Top color:</p>
          <input type="text" name="top" placeholder="Silver" />
          <p></p>
          {isLoading ? (
            <button type="submit" disabled>Submit</button>
          ) : (
            <button type="submit">Submit</button>
          )}
        </form>
      </main>

      <Perfume isLoading={isLoading} error={error} perfume={perfume} />

      <footer className={styles.footer}>
      </footer>
    </div>
  );
}
