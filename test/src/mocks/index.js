import getOrderItemsResponse from '../../res/getOrderItemsResponse.json' with { type: 'json' }
import express from 'express'

const app = express()
const port = 3000

app.get('/orders/v0/orders/:orderId/orderItems', (req, res) => {
    res.json(getOrderItemsResponse)
})

app.post('/auth/o2/token', (req, res) => {
    res.json({
        access_token: "accessToken",
        refresh_token: "refreshToken",
        token_type: "bearer",
        expires_in: 3600
    })
})

app.listen(port, () => {})