import { env } from '@/env.js'
import jwt from 'jsonwebtoken'

export type jwtPayload = {
    userId : number,
    email : string
}

export default async function generateToken(payload : jwtPayload) {
    const token = jwt.sign(
        payload,
        env.JWT_SECRET,
        {
            expiresIn : env.JWT_EXPIRES_IN
        }
    )
    return token
}