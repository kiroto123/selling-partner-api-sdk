import express from 'express'
import ordersApi from './mocks/orders-api.js'

const app = express()
const port = 3000

app.post('/auth/o2/token', (req, res) => {
    res.json({
        access_token: "accessToken",
        refresh_token: "refreshToken",
        token_type: "bearer",
        expires_in: 3600
    })
})

app.use('/orders/v0', ordersApi)

app.listen(port, () => {})