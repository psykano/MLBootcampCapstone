import React, { useState } from "react";
import Image from "next/image";

export default function Perfume({ isLoading, error, perfume }) {
  return (
    <>
      <div>
        <ShowLoading isLoading={isLoading} />
        <ShowError error={error} />
        <ShowPerfume perfume={perfume} />
      </div>
    </>
  )
}

function ShowLoading({ isLoading }) {
  if (isLoading) {
    return (
      <>
        <p>Loading...</p> 
        <Image 
          src="/spinner.gif"
          width={100}
          height={100}
          alt="Loading spinner"
        />
      </>
    )
  }
}

function ShowError({ error }) {
  if (error) {
    return (
      <p>{error}</p>
    )
  }
}

function ShowPerfume({ perfume }) {
  if (perfume) {
    return (
      <Image
        src={perfume}
        width={512}
        height={512}
        alt="AI generated perfume"
      />
    )
  }

}