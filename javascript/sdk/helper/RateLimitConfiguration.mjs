export class RateLimitConfiguration {
    /**
     * RateLimiter Permit: requests per second
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
     * Burst value
     * @type {number}
     * @private
     */
    #burstRequests;

    /**
     * @param {number} rateLimitPermit
     * @param {number} waitTimeOutInMilliSeconds
     * @param {number} burstRequests
     */
    constructor(rateLimitPermit, waitTimeOutInMilliSeconds, burstRequests = null) {
        this.#rateLimitPermit = rateLimitPermit;
        this.#waitTimeOutInMilliSeconds = waitTimeOutInMilliSeconds;
        this.#burstRequests = burstRequests;
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

    /**
     * @returns {number}
     */
    getBurstRequests() {
        return this.#burstRequests;
    }

    /**
     * @param {number} burstRequests
     */
    setBurstRequests(burstRequests) {
        this.#burstRequests = burstRequests;
    }
}