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
      const apiKey = process.env.API_KEY
      const apiUrl = process.env.API_URL
      const data = {key: apiKey, color: req.body.color, shape: req.body.shape, top: req.body.top}
      const response = await fetch(apiUrl,{
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'content-type': 'application/json'
        }
      })
      let rbody = await response.json();
      if (rbody.image) {
        res.status(200).json({ image: rbody.image })
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
