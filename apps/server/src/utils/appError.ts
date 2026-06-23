export class AppError extends Error {
    readonly statusCode: number
    readonly status: boolean

    constructor(message: string, statusCode: number, status = true) {
        super(message)

        this.name = this.constructor.name
        this.statusCode = statusCode
        this.status = status
    }

    // Convenience factories
    static badRequest(message: string) {
        return new AppError(message, 400)
    }

    static unauthorized(message: string) {
        return new AppError(message, 401)
    }

    static notFound(message: string) {
        return new AppError(message, 404)
    }

    static internal(message: string) {
        return new AppError(message, 500, false)
    }
}