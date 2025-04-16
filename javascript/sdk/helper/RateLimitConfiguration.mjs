export class RateLimitConfiguration {
    /**
     * RateLimiter Permit
     * @type {number}
     * @private
     */
    #rateLimitPermit;

    /**
     * Timeout for RateLimiter
     * @type {number}
     * @private
     */
    #waitTimeOutInMilliSeconds;

    /**
     * @param {number} rateLimitPermit
     * @param {number} waitTimeOutInMilliSeconds
     */
    constructor(rateLimitPermit, waitTimeOutInMilliSeconds) {
        this.#rateLimitPermit = rateLimitPermit;
        this.#waitTimeOutInMilliSeconds = waitTimeOutInMilliSeconds;
    }

    /**
     * @returns {number}
     */
    getTimeOut() {
        return this.#waitTimeOutInMilliSeconds;
    }

    /**
     * @param {number} waitTimeOutInMilliSeconds
     */
    setTimeOut(waitTimeOutInMilliSeconds) {
        this.#waitTimeOutInMilliSeconds = waitTimeOutInMilliSeconds;
    }

    /**
     * @returns {number}
     */
    getRateLimitPermit() {
        return this.#rateLimitPermit;
    }

    /**
     * @param {number} rateLimitPermit
     */
    setRateLimitPermit(rateLimitPermit) {
        this.#rateLimitPermit = rateLimitPermit;
    }
}