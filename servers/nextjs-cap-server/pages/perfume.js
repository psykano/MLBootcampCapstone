import React, { useState } from "react";
import Image from "next/image";

export default function Perfume({ isLoading, error, perfume }) {
  return (
    <>
      <ShowLoading isLoading={isLoading} />
      <ShowError error={error} />
      <ShowPerfume perfume={perfume} />
    </>
  )
}

function ShowLoading({ isLoading }) {
  if (isLoading) {
    return (
      <>
        <div className="bg-gray-50 shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <p className="block text-blue-500 text-sm font-bold flex items-center justify-center">Loading...</p> 
          <Image 
            src="/spinner.gif"
            width={100}
            height={100}
            alt="Loading spinner"
          />
        </div>
      </>
    )
  }
}

function ShowError({ error }) {
  if (error) {
    return (
      <>
        <div className="bg-gray-50 shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <p className="block text-red-500 text-sm font-bold flex items-center justify-center">{error}</p>
        </div>
      </>
    )
  }
}

function ShowPerfume({ perfume }) {
  if (perfume) {
    return (
      <>
        <div className="px-8 pt-6 pb-8 mb-4">
          <Image
            src={perfume}
            width={512}
            height={512}
            alt="AI generated perfume"
          />
        </div>
      </>
    )
  }

}