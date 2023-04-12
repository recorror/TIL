import { StatusBar } from 'expo-status-bar';
import { Platform, SafeAreaView, StyleSheet, Text, View } from 'react-native';
import Header from './src/Header';
import {
  getStatusBarHeight,
  getBottomSpace,
} from 'react-native-iphone-x-helper';

import { SafeAreaProvider } from 'react-native-safe-area-context';

const statusBarHeight = getStatusBarHeight(true);
const bottomSpace = getBottomSpace();

// console.log(`${Platform.OS}: ${statusBarHeight}, ${bottomSpace}`);

export default function App() {
  return (
    // <View style={styles.container}>
    //   <Header />
    // </View>
    <SafeAreaProvider>
      <SafeAreaView edges={['right', 'bottom', 'left']}>
        <Header />
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     // paddingTop: statusBarHeight,
//     backgroundColor: '#fff',
//     // alignItems: 'center',
//     // justifyContent: 'flex-end',
//   },
// });
