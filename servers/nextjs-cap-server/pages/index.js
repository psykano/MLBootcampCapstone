import Head from "next/head";
import styles from "../styles/Home.module.css";
import React, { useState } from "react";
import Image from "next/image";

export default function Home() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [perfume, setPerfume] = useState(null)

  async function onSubmit(event) {
    event.preventDefault()

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
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to <a href="https://nextjs.org">Next.js</a> on Docker!
        </h1>

        <p className={styles.description}>
          Get started by editing{" "}
          <code className={styles.code}>pages/index.js</code>
        </p>

        <form onSubmit={onSubmit}>
          <p>Shape:</p>
          <input type="text" name="shape" />
          <p>Color:</p>
          <input type="text" name="color" />
          <p>Top:</p>
          <input type="text" name="top" />
          <button type="submit">Submit</button>
        </form>
      </main>

      <div>
        {(perfume && perfume.trim() !== '') &&
          <Image
            src={perfume}
            width={500}
            height={500}
            alt="Picture of the author"
          />
        }
      </div>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{" "}
          <img src="/vercel.svg" alt="Vercel Logo" className={styles.logo} />
        </a>
      </footer>
    </div>
  );
}
