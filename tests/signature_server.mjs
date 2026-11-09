// Fake Tingee Open API used by test_signature.py.
// Verifies requests exactly like open-api/src/utils.ts: body-parser JSON.parse (no body -> {}),
// timestamp yyyyMMddHHmmssSSS parsed in server local time (run with TZ=Asia/Ho_Chi_Minh), window -90s / +11m,
// then HMAC-SHA512(secretToken, `${timestamp}:${JSON.stringify(body)}`) === x-signature.
// Prints the port on stdout, answers { code, message, data: { body, message } }.
import { createHmac } from 'crypto'
import http from 'http'

const SECRET = process.argv[2]

const reply = (res, payload) => {
  res.writeHead(200, { 'content-type': 'application/json; charset=utf-8' })
  res.end(JSON.stringify(payload))
}

const server = http.createServer((req, res) => {
  const chunks = []
  req.on('data', c => chunks.push(c))
  req.on('end', () => {
    const raw = Buffer.concat(chunks).toString('utf8')
    let body = {}
    if (raw) {
      try {
        body = JSON.parse(raw)
      } catch {
        return reply(res, { code: '400', message: 'Invalid JSON' })
      }
    }

    const ts = req.headers['x-request-timestamp'] || ''
    if (ts.length !== 17) return reply(res, { code: '90', message: 'Timestamp is not in correct format.' })
    const m = ts.match(/^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{3})$/)
    if (!m) return reply(res, { code: '90', message: 'Timestamp is not in correct format.' })
    const requestTime = new Date(+m[1], +m[2] - 1, +m[3], +m[4], +m[5], +m[6], +m[7]).getTime()
    const now = Date.now()
    if (requestTime - now > 90 * 1000) return reply(res, { code: '91', message: 'Invalid request timestamp.' })
    if (now - requestTime > 11 * 60 * 1000) return reply(res, { code: '91', message: 'Request expired.' })

    if (!req.headers['x-client-id']) return reply(res, { code: '92', message: 'Client id not found' })

    const message = `${ts}:${JSON.stringify(body)}`
    const expected = createHmac('sha512', SECRET).update(message).digest('hex')
    if (req.headers['x-signature'] !== expected) {
      return reply(res, { code: '97', message: 'Invalid signature', data: { message } })
    }

    reply(res, { code: '00', message: 'Success', data: { method: req.method, url: req.url, body, message, userAgent: req.headers['user-agent'] } })
  })
})

server.listen(0, '127.0.0.1', () => {
  process.stdout.write(`${server.address().port}\n`)
})
