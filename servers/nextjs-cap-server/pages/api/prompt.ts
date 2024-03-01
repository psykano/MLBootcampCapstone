import type { NextApiRequest, NextApiResponse } from 'next'
 
type ResponseData = {
  image: string
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  if (req.method === 'POST') {
    try {
      console.log('got:')
      console.log(req.body)
      const apiKey = process.env.API_KEY
      const apiUrl = process.env.API_URL
      const body = {key: apiKey, color: req.body.color, shape: req.body.shape, top: req.body.top}
      const response = await fetch(apiUrl,{
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
          'content-type': 'application/json'
        }
      })
      if (!response.ok) {
        throw new Error('Failed to submit the data.')
      }
      const data = await response.json();
      if (data.image) {
        res.status(200).json({ image: data.image })
      } else {
        res.status(200).json({ image: '' })
      }
    } catch (error) {
      console.log(error)
      res.status(200).json({ image: '' })
    }

  } else {
    res.status(200).json({ image: '' })
  }
}
