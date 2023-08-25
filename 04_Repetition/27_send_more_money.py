# send_more_money.py
for s in range(1,10):
    for e in range(0,10):
        for n in range(0,10):
            for d in range(0,10):
                for m in range(1,10):
                    for o in range(0,10):
                        for r in range(0,10):
                            for y in range(0,10):
                                send = s*1000+e*100+n*10+d
                                more = m*1000+o*100+r*10+e
                                money = m*10000+o*1000+n*100+e*10+y
                                if send + more == money:
                                    if s!=e and s!=n and s!=d and s!=m and s!=o and s!=r  and s!=y and \
                                       e!=n and e!=d and e!=m and e!=o and e!=r and e!=y and \
                                       n!=d and n!=m and n!=o and n!=r and n!=y and \
                                       d!=m and d!=o and d!=r and d!=y and \
                                       m!=o and m!=r and m!=y and \
                                       o!=r and o!=y and \
                                       r!=y:
                                        print("  {:d}{:d}{:d}{:d}".format(s,e,n,d))
                                        print(" +{:d}{:d}{:d}{:d}".format(m,o,r,e))
                                        print("——")
                                        print(" {:d}{:d}{:d}{:d}{:d}".format(m,o,n,e,y))
