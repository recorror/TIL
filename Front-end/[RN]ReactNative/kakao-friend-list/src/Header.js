import { View, Text } from 'react-native';
import { StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
{
  /* <Ionicons name="search-outline" size={24} color="black" />
<Ionicons name="person-add-outline" size={24} color="black" />
<Ionicons name="md-musical-notes-outline" size={24} color="black" />
<Ionicons name="ios-settings-outline" size={24} color="black" /> */
}

const IconButton = (props) => {
  <View style={{ paddingHorizontal: 6 }}>
    <Ionicons name={props.name} size={24} color='black' />
  </View>;
};

export default () => {
  return (
    <View style={styles.headerContainer}>
      <Text style={styles.title}>친구</Text>
      <View style={{ flexDirection: 'row' }}>
        <IconButton name='search-outline' />
        <IconButton name='person-add-outline' />
        <IconButton name='md-musical-notes-outline' />
        <IconButton name='ios-settings-outline' />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  headerContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 10,
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
  },
});
