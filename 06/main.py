from collections import deque

my_input = 'hlfhfzffqnnrlnnvnmmgbgwgttbppcrcnnmdmfdmmgwwrrqnrrscrctcbttvcvtvvhchjhccjgjttmddplplqplqlbqlblrrbrvvprpffpmmzpmpcczjzzbwwfssvrrvggncgncgcwczzswwqqjjflffpwfpwpbwpwpdpbpvvqffcfcjffjllncczfzzmhzzmddgdrgrwwjzzdjjsnjsjfsjsjhhcchlccchqchhzzpnngdgndnpnppsdsggbvgvgpprqrqmmlzmzllvrrcvclcwczcqqcdcfcqqmmzbzdzdjzdjdmjdjzdjjcvjvcjvcvssltstttfbtftrfrlrdllrqqfssslccjdcjdjfdjfjqjnqjnjnrnddtnndtnnztzqztqztqzzpmzmggzrgrwwdqwdwcdwdnnmlmgmtmtstwssbffcnclclnclcjjcjpcpqcpqcpqpmqqfccpcjppnspsnnzggnpntndtdqtthwhnhwnwllzhlzhlzzghzghhlhvhwhjhfjjcnjnvjnjvvqccdmmgddllnmnrrdtdnncggfhgfglfgfmfnnpvvggznnwvnwwfgghrrfwrwzwszzzldzdldhlhblhblhbbbgjgsjggmqqmrrzggrhhwpwdpwdpwplpgpbggtssqffbqfbqbnnsqnqfnngcnnmwnmnbmmmslsjllbtbbpllltzzhgzztllsdllrvvhvjvbbhcbhchmchcctbcttvccgwcwpcchrcrdrdggcrrntrrfllcffbdfflrrrgbgrbbbdqbqjbbgbgrrqwqtwqwhwghwhzwwcswsnwnqqjhjhwhfwhffdfgddgjgsjgjhgglhlwhlhssfqfhhdmdnmnppdcddfzzhmhqqntqnnjvnjvjddcvcgcbgbbpjbjtbjjfgftgffplljfjrrhqqpddlssrvsrvrpppsllsdsqqqzzfttqsqzssjbbrnbnnrbbsrshsrrshrhwhbwbrrsrfrttfqtfqqfddvrvjrjvjsjhjsjdjqdjjlqjjjgcjcmcncfcrcwrwsrsslffzszmsszrsssrnrjjvbvpvcppptbbhhrddbcbggbqbmmsqqwggfpfbblmldmmpmwpwfwjfjsjnjmmpllccjzcjcwwpswshhpthhzchctcbcrrrrmvrvrdvvjmmvgmgwglghllvmllzlzzsvzzrmmhnnsjnnpvpwvpwwmvwwdqqdffhhhmccfgfvggchcctrrmdrrhrhnhnzzgpzzgttnhthvhzzqvvvwpwqpqdppsnnrgnnhphphmhcmcrmrvvqlvqqsccqhchzhwwmvmzmczzgsgdsggthgglrlnrlllbdllhwlwltwwcswsgssbhbsbvsbsbwbhbnncrcllttbrbppjccfpfhhgshschsccmrcmmcrrrzvvrcrggmwgwjwnwjjbffjddjnjgngqgdgnndznndvvfqfgfvvrvqrvvpllnsszbsbdbbdzbdbzbqbzznrznzjzpptcptccvwccfscffrftrrsnsvvswvvhbhzzfbzffncchhcnngzzcpcmmfttsntnjjsccqbcqqmzzgppdhppdtppmffgtgvvlzlpptdtttdppqjqtqctcrrzsswwtnwtnwnqqvbbdgjhvmmzpnhfvsbddzhgdwcnfdstvhhbzlzcfjwhlptbhmbmblprtsdmrdhbbbwpplnzgdnrzjmgzgpqbggnqvwwtntzgfwqrztqtdrsnhpfzswptggnvbszdcrmrhhtlrrfnpqrnpwrbmhlfwmdqqdbqrwbzqjbzwrgmbgrtzrhdclqfgsrtsgfwqrnnqgwsncmpgffggssrqvwjlhpsghbqdtzwmvzzvcmzsjqvprvcqwqjbcqcqrhpwwcsrscgmfdppbgvmnrdfrppblznbstnjzwwgstjvtprjbhtpdfgrhdjnjmnlbfwggzhcngvcwvcfpcwdtdppwjrdzsnjlnrzbfqqshlnzvwsmscgpfwjzhtwgfwgzdhbdwwzbsmfwwbmvrlrpswnjlmfbfzhwvcmgwfzssmmtjlwtrpwpwgnspbgchdncbfcpjsvtzjqtwqwjwgbhrbwvhqbcstsgsnwsjmhrlrvzgqhqfrmnrjdrhdjwcwctpdrzctlvnfzmzwhsnfprlzgzjpqvzchlmvbhffhpfjtvsdbvbdmwgvmqpflhwwndbqthmmwshdtspsrvqdflmmzwbqbqmpfdwjmvpbzdnqzfmhzdgldqjjvgpfcqftvjzwnzmfqdggrwlfzdhjnhmtrjbnllgqpntwmhnwtglnqdwbqdblpwnnrdwzpsqzfwqcmhqhnpsdcwvdldphgnrtqzdbnnzdzfttldrqcztlvlrgpdqzrcthslmtqhfvbzrfgnlrprcpbsctqhspbhnjtzrzhqjzszbzdthttqmbznzssftztwlggmdqqdtfllqjzjtvpgjfhtbwtbmtjplqnbdmsvlnqcwtdbdvfjnzgsmpnhbvvwwfbrgffjqfsccdjdwvbsdhqwfzvcpjzjbdjgrdctjplhwbdhhnbnwstvndnnwtsgbhzbvwdshvmnbwsthlrggtmddvjbfzfrnrdrqfjpslrccctzpjbwpdbhlbzfmwbltcqfngdprvfhgcszdtpnrcpdmllfnlspgrdrpwqmqbmrglvlrsmrfqrtzzgjcvqtqzpmghjrvmdmvvqztrjzbzjwdqsmrwpqnswbzhjbzzhdvmnfdsztzdzrjssgnnfqvbtsqrrmcppjgrmnstrnrlwjvvcczqlcbmwqzdfpssfwdfrvwtstwchdgwtrhhcmppcqlmrqlnwqccfphsdhbsbmtjvpcwwjrmrllbpnrmpbvwgwbftpdpphccwqcblcnvvbbppscmnjqgddllbnbvmmqzdffrrjtqwllzgpqrmnlfqrptzqmdmnrfnjpvqvjbsqrhljslgqqcqqtmtbwjrpphtjgjbqpzmzrzjrfjwcdcnbsjfljclffjplnrrcfbmhphtcjrzlrvvjcznpgpnrdwwqvgnbnzqnlcghhgwvhqbvjzfbdvhrzlqfbtlqhpltfjlfpbnjbphmmpntzqgjmwjtchwmlwvfjmfflqzpqnvvrgnbddzlfpdpdjghfgbsfddjspnfdwvqppncmdgfrnvrpcrflhgjgbwdsbwblfcwbtlrrnjjdhbvmrzgsvjwgfnnhqfbvhprlmwwqgclzlbqbrdspcbhftmdscsmpwrggrmnsvjphjmzmmrlrhnmdhwjlbmjchtvsrcplfspsssjznmzcrqnsjjtwjzvlhshbptqwwvjhjvzrhphphsbphpnzpfbwcdnqrhrrvlrwrztlpqnrcfzrncsvpzqzgslrlrwhvtgjmfncldqmvshlmnlpqbgvnwqfcthgrgllmqrjqmfgznspgltpptglpdcvhtzsprprbldbzhbmjsqzwvjggwhsczltcvgwqhspzpzvljwqjgrgtwswjdswlzjzslrsslvqzncjwhbbjpbdthqpgmhfglggmlrgwdsplgscrwstntvrhjzjjlshtgmnnhvsjwfmcjbpzjcstmnpvtbgrfcfdwjljsrfhdphrdcslwhgvlnwltwchplvfzntfgcnlsvzrvnnczhhqdlwjvqprhmtjdtwmppffmszzzqtfrgnhnzqgqzhrjzgntcszstrfhhtptgvswvzvjcgcntmhzzmdgsmtgzhpfvqfnwmsjdhtfgmmbrrfsdlptchqqzqdqjncmtpznfssrcnmcdnthglmfzsfgltrndqsfmdftmfgchbwmzgrtjvgqtshlltthnnpqnzfrchzhdzrrnpzvfzblrmhwdwjnqdptlbvndmmlhzhvsfdlmlhqrgqqzsdqtpczwcrwcbsftvvphfbwjrvrnrcqbbcsqgnhltwzvllljcvpwjgslbmngcdmpdvjlgcnrzwqjdgrblncpqmrgjmpqjzvdmcmwfnwqlszdgwqdfznhsnpsjrfwrqpqmpvhstmzgqblfmcfvwljbhdfhdmqcvrwnqcstwtzgmng'

def find_marker(buffer, n):
    # Use a deque to store the last n characters seen.
    last_n = deque()

    # Iterate through the buffer one character at a time.
    for i, c in enumerate(buffer):
        # Add the current character to the deque.
        last_n.append(c)
        if len(last_n) > n:
            # If we have more than n characters, remove the oldest one.
            last_n.popleft()

        # If the last n characters are all different, we have found the marker.
        if len(set(last_n)) == n:
            # Return the number of characters processed so far.
            return i + 1

# Test the function with the examples from the problem description.
'''
print(find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4))  # 7
print(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4))  # 5
print(find_marker('nppdvjthqldpwncqszvftbrmjlhg', 4))  # 6
print(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4))  # 10
print(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4))  # 11
'''

print(find_marker(my_input, 4))
print(find_marker(my_input, 14))