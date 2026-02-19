# My Entries are expired, why is the dashboard still showing active instances?

This is normal behaviour. Unless active lease reaping is enabled (see the install guide for your particular distribution) Blitz will only lazily delete expired Entry's and update statistics. Even when active lease reaping is enabled the stats can still be out of date though they will be at their most accurate just after Blitz has performed an active reap.
