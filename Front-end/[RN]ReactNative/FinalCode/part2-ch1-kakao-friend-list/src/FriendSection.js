import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import { MaterialIcons } from '@expo/vector-icons';

export default (props) => {
  return (
    <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
      <Text style={{ color: 'grey' }}>친구 {props.friendProfileLen}</Text>

      {/* 화살표 클릭할 수 있는 부분. */}
      <TouchableOpacity onPress={props.onPressArrow}>
        <MaterialIcons
          name={props.isOpened ? 'keyboard-arrow-up' : 'keyboard-arrow-down'}
          size={24}
          color='lightgrey'
        />
      </TouchableOpacity>
    </View>
  );
};
