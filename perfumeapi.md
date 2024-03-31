## Create Perfume

Used to create an AI generated perfume

**URL** : `/api/prompt`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "color": "[valid string]",
    "shape": "[valid string]",
	"top": "[valid string]"
}
```

**Data example**

```json
{
    "color": "red",
    "shape": "square",
	"top": "silver"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "image": "http://res.cloudinary.com/dexgq3cxv/image/upload/3PXnUxXpf3gaRgJnYTi8XZ"
}
```

## Error Response

**Condition** : If any of 'color', 'shape', 'top' is an invalid string or if the machine learning server is down. An empty image URL will be returned.

**Code** : `200 OK`

**Content** :

```json
{
    "image": ""
}
```