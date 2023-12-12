/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
                source:"/api/:slug*",
                destination: "http://127.0.0.1:5555/:slug*",
            },
        ];
    },
}

module.exports = nextConfig
