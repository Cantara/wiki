# Dashboard is showing inaccurate or negative instance counts - whats wrong?

Nothing....

The dashboard provides only an approximation of the current state of the Blitz engine. Forcing the statistics to be 100% accurate would impact performance significantly and cannot be guarenteed in various circumstances (in particular in respect of lease cleanup).

Statistics are generated concurrently alongside all other activity and can, for example, include counts derived from a partially committed transaction (that is, one that is in the process of being committed).
